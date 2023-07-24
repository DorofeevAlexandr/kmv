from pymodbus import pymodbus_apply_logging_config
from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusException
from pymodbus.pdu import ExceptionResponse
from pymodbus.transaction import (
    #    ModbusAsciiFramer,
    #    ModbusBinaryFramer,
    ModbusRtuFramer,
    ModbusSocketFramer,
    ModbusTlsFramer,
)


def run_sync_client(host=None, port=None):
    """Run sync client."""

    # activate debugging
    pymodbus_apply_logging_config("DEBUG")


    client = ModbusSerialClient(
        method='rtu',
        port='/dev/ttyS0',
        baudrate=9600,
        framer=ModbusRtuFramer,
        timeout=10,
        retries=3,
        retry_on_empty=False,
        close_comm_on_error=False,
        strict=True,
        bytesize=8,
        parity="N",
        stopbits=1,
        handle_local_echo=False,
    )

    print("connect to server")
    client.connect()
    print('------------------')

    print("get and verify data")
    try:
        rr = client.read_coils(1, 1, slave=106)
    except ModbusException as exc:
        print(f"Received ModbusException({exc}) from library")
        client.close()
        return
    if rr.isError():
        print(f"Received Modbus library error({rr})")
        client.close()
        return
    if isinstance(rr, ExceptionResponse):
        print(f"Received Modbus library exception ({rr})")
        # THIS IS NOT A PYTHON EXCEPTION, but a valid modbus message
        client.close()

    print("close connection")
    client.close()


if __name__ == "__main__":
    run_sync_client()