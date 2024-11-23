import subprocess


def get_aos_device():
    """
    Return Connected Device' S/N
    :return device_serial_number:
    """
    try:
        # Execute "adb devices"
        cmd = 'adb devices'
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()
        device_sn = ""

        # Get All of Connected Devices
        output = out.decode().splitlines()

        # Get device info per line
        if len(output) > 0:
            device_sn = output[1].split()[0]
            print("DEVICE SERIAL NUMBER  : ", device_sn)
            return device_sn
        else:
            print("No Connected Devices Found...")
            return device_sn
    except:
        print("Couldn't Find Any Connected Devices")

