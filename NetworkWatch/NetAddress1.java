package NetworkWatch;
import java.net.*;

class NetAddress1 {
    public static void main(String[] args) throws Exception {
        InetAddress ip;
        ip = InetAddress.getLocalHost();
        NetworkInterface network = NetworkInterface.getByInetAddress(ip);
        InetAddress localhost = InetAddress.getLocalHost();
        NetworkInterface networkinterface = NetworkInterface.getByInetAddress(localhost);
        
        

        System.out.println("Subnet Mask: " + networkinterface);
        System.out.println("Local Host: " + localhost);
        
    }
}

class MacAddress {
    public static void mac(String[] args) throws Exception {
        byte [] mac = network.getHardwareAddress();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < mac.length; i++) {
            sb.append(String.format("%02X%s",
            mac[i], (i < mac.length - 1) ? "-" : ""));
        }

        System.out.println("MAC: " + sb.toString());
    }
}