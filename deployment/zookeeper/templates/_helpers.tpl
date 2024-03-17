{{/* 
Define a function to generate zookeeper container environment variables 
*/}}
{{ define "zookeeper.envVars" }}
            - name: ZOOKEEPER_CLIENT_PORT
              value: "2181"
            - name: ZOOKEEPER_SERVER_ID
              valueFrom:
                fieldRef:
                  fieldPath: metadata.uid
            - name: ZOOKEEPER_TICK_TIME
              value: "2000"
            - name: ZOOKEEPER_INIT_LIMIT
              value: "10"
            - name: ZOOKEEPER_SYNC_LIMIT
              value: "5"
{{- end -}}

