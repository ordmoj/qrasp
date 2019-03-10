# set_backend
# Used to set a valid IBM Q backend to run on.

# Import the required tools
from sense_hat import SenseHat
hat = SenseHat()
from qiskit import IBMQ, Aer, execute
import Qconfig_IBMQ_experience
# from qiskit.tools.monitor import job_monitor

# Enable the account based on the stored API key
IBMQ.enable_account(Qconfig_IBMQ_experience.APItoken)

# Add status here...

# Set the backend
def set_backend(back):
    global backend
    if back == "ibmq":
        backend = IBMQ.get_backend('ibmqx4')
    else:
        backend = Aer.get_backend('qasm_simulator')    
    print(backend)
#hat.show_message(backend.name())
