from prometheus_api_client import PrometheusConnect
import time

#   create a PrometheusConnect instance
prom = PrometheusConnect(url="http://192.168.56.10:31882")
# prom_openfaas = PrometheusConnect(url="http://192.168.56.11:30424")


#   1. The actual CPU, memory, network (sum of network
#   bytes received and transmitted) and disk I/O (sum of disk
#   read and write bytes) bandwidth utilization of each of the
#   nodes in the cluster at time 𝑡
node_cpu_utilization = prom.custom_query('100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[1m])) * 100)')
node_memory_utilization = prom.custom_query('100 - ((node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100)')
node_disk_io_utilization = prom.custom_query('sum by (instance) (irate(node_disk_read_bytes_total[1m]) + irate(node_disk_written_bytes_total[1m]))')
node_network_utilization = prom.custom_query('sum by (instance) (irate(node_network_receive_bytes_total[1m]) + irate(node_network_transmit_bytes_total[1m]))')

# #   2. The CPU and memory capacities of each of the nodes in the cluster
# node_cpu_capacity = prom.custom_query('count without(cpu, mode) (node_cpu_seconds_total{mode="idle"})')
# node_memory_capacity = prom.custom_query('node_memory_MemTotal_bytes')

# #   3. Unit price of each cluster node

# #   4. The total of minimum CPU and memory requested by function instances
# #   running in each node at time 𝑡

# cpu_request_sum_by_node_results = prom.custom_query('sum by (node) (kube_pod_container_resource_requests{namespace="openfaas-fn", resource="cpu"})')
# memory_request_sum_by_node_results = prom.custom_query('sum by (node) (kube_pod_container_resource_requests{namespace="openfaas-fn", resource="memory"})')

# #   5. The active status of each node. A node is considered
# #   to be active at time 𝑡 if it contains instances of functions for
# #   which user requests are received at the cluster at the time
# active_status_results = prom.custom_query('count(kube_pod_info{namespace="openfaas-fn"}) by (node)')

# #   6. The number of replicas of function of type 𝑝ₖ already deployed on each node
# function_k_replicas = 'count(kube_pod_container_info{namespace="openfaas-fn", container="chameleon"}) by (node)'
# function_k_replicas_results = prom.custom_query(function_k_replicas)

# #   7. The minimum CPU and memory requested by the function instance 𝑝ⱼᵏ
# function_cpu_request_results = prom.custom_query('kube_pod_container_resource_requests{namespace="openfaas-fn", resource="cpu", container="chameleon"}')
# function_memory_request_result = prom.custom_query('kube_pod_container_resource_requests{namespace="openfaas-fn", resource="memory", container="chameleon"}')

# #   8. Sum of network bytes received and transmitted during a single request 
# #   execution of 𝑘ᵗʰ function on average
# function_bytes_received = prom.custom_query('container_network_receive_bytes_total{namespace="openfaas-fn", pod=~"chameleon.*"}')
# function_bytes_received_result = function_bytes_received[0]
# function_bytes_received_result = function_bytes_received_result['value'][1]

# function_bytes_transmitted = prom.custom_query('container_network_transmit_bytes_total{namespace="openfaas-fn", pod=~"chameleon.*"}')
# function_bytes_transmitted_result = function_bytes_transmitted[0]
# function_bytes_transmitted_result = function_bytes_transmitted_result['value'][1]

# # number of invocations of 𝑘ᵗʰ function
# num_of_invocations = prom_openfaas.custom_query('gateway_function_invocation_total{code="200", function_name="chameleon.openfaas-fn"}')
# num_of_invocations_value = num_of_invocations[0]
# num_of_invocations_value = int(num_of_invocations_value['value'][1])

# #   9. Sum of disk read and write bytes during a single request 
# #   execution of 𝑘ᵗʰ function on average
# disk_reads_bytes = prom.custom_query('container_fs_reads_bytes_total{container="random-disk-io"}')
# disk_reads_bytes_results = disk_reads_bytes[0]
# disk_reads_bytes_results = int(disk_reads_bytes_results['value'][1])

# disk_writes_bytes = prom.custom_query('container_fs_writes_bytes_total{container="random-disk-io"}')
# disk_writes_bytes_results = disk_writes_bytes[0]
# disk_writes_bytes_results = int(disk_writes_bytes_results['value'][1])

# #   10. Request concurrency on each function instance of type 𝑝ᵏ
# num_of_replicas = prom.custom_query('count(kube_pod_info{namespace="openfaas-fn", pod=~"chameleon.*"})')
# num_of_replicas_value = num_of_replicas[0]
# num_of_replicas_value = int(num_of_replicas_value['value'][1])

#   11. Relative function response time (RFRT) of function
#   of type 𝑝ᵏ in the cluster at time 𝑡. This is the ratio between
#   the actual and standard response time (𝑟₀ᵏ) for the function

#   12. The request arrival rates for each different function
#   deployed in the cluster at time 𝑡

