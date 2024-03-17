#
    Deploy
#

####
    helm upgrade-i kafka /deployment/kafka
    helm upgrade-i zookepr /deployment/zookepr
####

####
    apt install python3-kafka # for scripts
    build the image:
        docker build -t py_script:latest .
    deploy the image:
        kubectl apply -f healthcheck-service.yaml
####