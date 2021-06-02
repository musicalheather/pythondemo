Temperature Calculations for the masses!

http://converter.bowespythondemo.com/

1. Dive into HTML
2. Find a happy medium of training for Python
3. Started with the python app first
4. Left Kubernetes till the end
5. Asked Cliff for help earlier



EKS instructions

EKS Cluster & nodegroup Creation:
=============================

- Make sure using latest eksctl version.
$ eksctl version
0.51.0

- Created EKS cluster through eksctl command line utility.

$ eksctl create cluster --version 1.19 --name Testingcluster
2021-05-23 12:02:46 [ℹ]  eksctl version 0.51.0
2021-05-23 12:02:46 [ℹ]  using region ap-south-1
2021-05-23 12:18:49 [✔]  EKS cluster "Testingcluster" in "ap-south-1" region is ready

Updated kubeconfig file:
=====================

$ aws eks update-kubeconfig --name Testingcluster
Added new context arn:aws:eks:ap-south-1:123456789012:cluster/Testingcluster to /Users/user1/.kube/config

Listed down the running worker nodes:
================================

$ kubectl get nodes
NAME                                            STATUS   ROLES    AGE    VERSION
ip-192-178-40-116.ap-south-1.compute.internal   Ready    <none>   101m   v1.19.6-eks-49a6c0
ip-192-178-80-211.ap-south-1.compute.internal   Ready    <none>   101m   v1.19.6-eks-49a6c0

OIDC-provider Creation:
====================

$ eksctl utils associate-iam-oidc-provider --cluster Testingcluster --approve
2021-05-23 14:01:20 [ℹ]  eksctl version 0.51.0
2021-05-23 14:01:20 [ℹ]  using region ap-south-1
2021-05-23 14:01:22 [ℹ]  will create IAM Open ID Connect provider for cluster "Testingcluster" in "ap-south-1"
2021-05-23 14:01:23 [✔]  created IAM Open ID Connect provider for cluster "Testingcluster" in "ap-south-1"

Downloaded aws-load-balancer-controller policy:
========================================

$ curl -o iam_policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.2.0/docs/install/iam_policy.json
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  7273  100  7273    0     0   8063      0 --:--:-- --:--:-- --:--:--  8054


Created aws-load-balancer-controller policy:
====================================

$ aws iam create-policy \
>     --policy-name DemoAWSLoadBalancerControllerIAMPolicy \
>     --policy-document file:///Users/user1/iam_policy.json
{
    "Policy": {
        "PolicyName": "AWSLoadBalancerControllerIAMPolicy",
        "PolicyId": "ABCDERTYV22M6YAB",
        "Arn": "arn:aws:iam::123456789012:policy/AWSLoadBalancerControllerIAMPolicy",
        "Path": "/",
        "DefaultVersionId": "v1",
        "AttachmentCount": 0,
        "PermissionsBoundaryUsageCount": 0,
        "IsAttachable": true,
        "CreateDate": "2021-05-23T08:34:03+00:00",
        "UpdateDate": "2021-05-23T08:34:03+00:00"
    }
}


Created iamserviceaccount:
=======================

$ eksctl create iamserviceaccount \
>   --cluster=Testingcluster \
>   --namespace=kube-system \
>   --name=aws-load-balancer-controller \
>   --attach-policy-arn=arn:aws:iam::123456789012:policy/AWSLoadBalancerControllerIAMPolicy \
>   --override-existing-serviceaccounts \
>   --approve 
2021-05-23 14:05:10 [ℹ]  eksctl version 0.51.0
2021-05-23 14:05:10 [ℹ]  using region ap-south-1
2021-05-23 14:05:13 [ℹ]  1 iamserviceaccount (kube-system/aws-load-balancer-controller) was included (based on the include/exclude rules)
2021-05-23 14:05:13 [!]  metadata of serviceaccounts that exist in Kubernetes will be updated, as --override-existing-serviceaccounts was set
2021-05-23 14:05:49 [ℹ]  created serviceaccount "kube-system/aws-load-balancer-controller"

Installed the AWS Load Balancer Controller using Helm:
=============================================

$ kubectl apply -k "github.com/aws/eks-charts/stable/aws-load-balancer-controller//crds?ref=master"
customresourcedefinition.apiextensions.k8s.io/ingressclassparams.elbv2.k8s.aws created
customresourcedefinition.apiextensions.k8s.io/targetgroupbindings.elbv2.k8s.aws created

$ helm repo add eks https://aws.github.io/eks-charts
"eks" has been added to your repositories

$ helm repo update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "eks" chart repository
Update Complete. ⎈Happy Helming!⎈

$ helm upgrade -i aws-load-balancer-controller eks/aws-load-balancer-controller \
>   --set clusterName=Testingcluster \
>   --set serviceAccount.create=false \
>   --set serviceAccount.name=aws-load-balancer-controller \
>   -n kube-system
Release "aws-load-balancer-controller" does not exist. Installing it now.
NAME: aws-load-balancer-controller
LAST DEPLOYED: Sun May 23 14:30:14 2021
NAMESPACE: kube-system
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
AWS Load Balancer controller installed!


$ kubectl get deployment -n kube-system aws-load-balancer-controller
NAME                           READY   UP-TO-DATE   AVAILABLE   AGE
aws-load-balancer-controller   2/2     2            2           23s


$ kubectl logs -n kube-system   deployment.apps/aws-load-balancer-controller
Found 2 pods, using pod/aws-load-balancer-controller-ff69446dd-6c7vb
{"level":"info","ts":1621760445.238206,"logger":"controller","msg":"Starting Controller","reconcilerGroup":"elbv2.k8s.aws","reconcilerKind":"TargetGroupBinding","controller":"targetGroupBinding"}
{"level":"info","ts":1621760445.2382433,"logger":"controller","msg":"Starting workers","reconcilerGroup":"elbv2.k8s.aws","reconcilerKind":"TargetGroupBinding","controller":"targetGroupBinding","worker count":3}
{"level":"info","ts":1621760445.2388153,"logger":"controller","msg":"Starting EventSource","controller":"ingress","source":"kind source: /, Kind="}
{"level":"info","ts":1621760445.2388444,"logger":"controller","msg":"Starting Controller","controller":"ingress"}
{"level":"info","ts":1621760445.2389476,"logger":"controller","msg":"Starting workers","controller":"ingress","worker count":3}

Deployed sample application:
=========================

$ kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.2.0/docs/examples/2048/2048_full.yaml
namespace/game-2048 created
deployment.apps/deployment-2048 created
service/service-2048 created

$ kubectl get pods -A
NAMESPACE     NAME                                           READY   STATUS    RESTARTS   AGE
game-2048     deployment-2048-79785cfdbb-4gzml               1/1     Running   0          36s
game-2048     deployment-2048-79785cfdbb-8d89z               1/1     Running   0          36s
game-2048     deployment-2048-79785cfdbb-9b6jl               1/1     Running   0          36s
game-2048     deployment-2048-79785cfdbb-v8gdn               1/1     Running   0          36s
game-2048     deployment-2048-79785cfdbb-vwjzv               1/1     Running   0          36s
kube-system   aws-load-balancer-controller-ff69446dd-6c7vb   1/1     Running   0          2m15s
kube-system   aws-load-balancer-controller-ff69446dd-mjl88   1/1     Running   0          2m15s
kube-system   aws-node-4szcd                                 1/1     Running   0          134m
kube-system   aws-node-dtfso                                 1/1     Running   0          134m
kube-system   coredns-758dbf67f7-hbvvu                     1/1     Running   0          141m
kube-system   coredns-758dbf67f7-wssdk                       1/1     Running   0          141m
kube-system   kube-proxy-44ifs                               1/1     Running   0          134m
kube-system   kube-proxy-49dfz                               1/1     Running   0          134m


$ kubectl get ingress/ingress-2048 -n game-2048
Warning: extensions/v1beta1 Ingress is deprecated in v1.14+, unavailable in v1.22+; use networking.k8s.io/v1 Ingress
NAME           CLASS    HOSTS   ADDRESS                                                                    PORTS   AGE
ingress-2048   <none>   *       k8s-game2048-ingress2-ae4093039a-1354425410.ap-south-1.elb.amazonaws.com   80      58m


$ kubectl describe ingress ingress-2048 -n game-2048
Warning: extensions/v1beta1 Ingress is deprecated in v1.14+, unavailable in v1.22+; use networking.k8s.io/v1 Ingress
Name:             ingress-2048
Namespace:        game-2048
Address:          k8s-game2048-ingress2-ae4093039a-1354425410.ap-south-1.elb.amazonaws.com
Default backend:  default-http-backend:80 (<error: endpoints "default-http-backend" not found>)
Rules:
  Host        Path  Backends
  ----        ----  --------
  *           
              /*   service-2048:80 (192.168.33.70:80,192.168.50.70:80,192.168.65.183:80 + 2 more...)
Annotations:  alb.ingress.kubernetes.io/scheme: internet-facing
              alb.ingress.kubernetes.io/target-type: ip
              kubernetes.io/ingress.class: alb
Events:
  Type    Reason                  Age    From     Message
  ----    ------                  ----   ----     -------
  Normal  SuccessfullyReconciled  2m13s  ingress  Successfully reconciled


Finally, I checked the load balancer output in browser and seen that its giving response(See the screen shoot for your reference)

If still didn't get resolve the issue, then please let me know I would reach out to service team on this behaviour and then will proceed further.

Have a great day ahead!

References:
[1] https://aws.amazon.com/premiumsupport/plans/developers/
[2] https://aws.amazon.com/premiumsupport/plans/