using System;
using System.Net.Sockets;
using System.Text;
using System.IO;


namespace goodChess1
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Player playerOne = new();
        }
    }

    public class Player
    {
        int serverPort = 9999;
        string serverIP = "192.168.0.49";
        public Player()
        {
            Console.Write("Player Name: ");
            string playerName = Console.ReadLine();
            TcpClient client = new TcpClient(serverIP, serverPort);
            string[] currentGames = decodemsg(sendMessage("playerName:"+playerName, client));
            createOrHost(currentGames, client);



        }
        
        
        
        void createOrHost(string[] currentGames, TcpClient client)
        {
            while (true){
                Console.WriteLine("1. Create a Game");
                Console.WriteLine("2. Join Game");
                Console.Write(">>");
                string option = Console.ReadLine();
                if (option == "1")
                {
                    sendMessage("createGame", client);
                }
                else if (option == "2")
                {
                    Console.WriteLine("Avalible Games:");
                    for (int i = 0; i < currentGames.Length; i++)
                    {
                        Console.WriteLine("\t " + (i + 1) + "." + currentGames[i]);
                    }
                    Console.WriteLine("Pick What Game You Want To Join, or 99 to got back");
                    Console.Write(">>");
                    option = Console.ReadLine();
                    if ((currentGames.Length + 1) >= int.Parse(option))
                    {
                        sendMessage("", client);
                    }
                }
            }
        }

        string sendMessage(string msg, TcpClient client)
        {

            //buffers the msg to be sent
            int byteCount = Encoding.ASCII.GetByteCount(msg + 1);
            Byte[] DataToSend = new Byte[byteCount];
            DataToSend = Encoding.ASCII.GetBytes(msg);

            //sends data(msg)
            NetworkStream stream = client.GetStream();
            stream.Write(DataToSend, 0, DataToSend.Length);
            //Console.WriteLine("[*] Sent Data: " + msg);

            //waits for response
            StreamReader sr = new StreamReader(stream);
            string response = sr.ReadLine();
            return response;
        }
        string[] decodemsg(string msg)
        {
            return msg.Split(":");
        }
    }
}