<<<<<<< HEAD
import multiprocessing
from tcp_client import tcp_client_main
from graphing_final import graphing_main
import time

if __name__ == "__main__":

    voltage = multiprocessing.Value('d', 0.0)

    p_tcp_client = multiprocessing.Process(target=tcp_client_main, args=(voltage,))
    p_graphing = multiprocessing.Process(target=graphing_main, args=(voltage,))

    p_tcp_client.start()
    time.sleep(2)
    p_graphing.start()

    p_tcp_client.join()
    p_graphing.terminate()

    
=======
from adc import adc_main
from tcp_server import tcp_server_main
import multiprocessing

if __name__ == "__main__":
    
    #create shared memory value to store voltage read by adc
    vin = multiprocessing.Value('d', 0.0)
    
    # create processes
    p_adc = multiprocessing.Process(target=adc_main,args=(vin,))
    p_tcp_server = multiprocessing.Process(target=tcp_server_main,args=(vin,))
    
    # start processes
    p_adc.start()
    p_tcp_server.start()
    
    # wait for processes to end
    p_tcp_server.join()
    p_adc.terminate()
    p_adc.join()
    
    #print("voltage: " + str(vin.value))
>>>>>>> 669dcbd55d31faa668d22dfaaaee36b883d8e52c
