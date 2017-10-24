import pika, os

def on_request(ch, method, props, body): #process and reply function
        request_param = int(body)# retrieve input parameters
        response = doSomething(request_param) #process the message
        ch.basic_publish(exchange='', #reply
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(
correlation_id = props.correlation_id),
                         		body=str(response))
        ch.basic_ack(delivery_tag = method.delivery_tag) #acknowledge 

url = os.environ.get('CLOUDAMQP_URL', 'amqp://mmiytlrk:NI3f6TaHj8L6nElruBzrx25fL-pcYvMG@lark.rmq.cloudamqp.com/mmiytlrk')
params = pika.URLParameters(url)
parmas.socket_timeout = 5

# initiate the connexion and setup the communication channel
connection = pika.BlockingConnection(params) 
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')
# wait for requests
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')
