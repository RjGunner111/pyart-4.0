using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Net;
using System.Net.Sockets;
using System.Threading.Tasks;
using System.Threading;
using System.Windows.Forms;

namespace pyart_4._0
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();  
        }
        private string ptsd;
        public static int choice;
        private string colony;
        public string wtshit;
        private string excheck;
        private string stifa;
        private string nowhere;
        private string changed;
        private string numlol;
        private string lmfo;
        public int chpk;
        public static int lmap;
        public static int lass;
        public int loopss;
        public string askd;
        private int shit;
        public int shutdown;
        private int enume;
        private int R;
        private int G;
        private int B;
        private byte[] msg;

        private void Form1_Load(object sender, EventArgs e)
        {
            shit = 0;
            AddToList();
            StartClient("recon", 1234);
            ThreadStart serv = new ThreadStart(start);
            Thread sharv = new Thread(serv);
            sharv.Start();
        }

        private void start()
        {
            string _port = "5555";
            byte[] buffer = new Byte[1024];
            IPEndPoint localEndPoint = new IPEndPoint(IPAddress.Parse("127.0.0.1"), int.Parse(_port));
            Socket listener = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);

            listener.Bind(localEndPoint);

            try
            {
                while (shutdown != 1)
                {
                    listener.Listen(10);

                    Socket socket = listener.Accept();
                    string data = null;

                    int bytesRec = socket.Receive(buffer);
                    data += Encoding.ASCII.GetString(buffer, 0, bytesRec);

                    while (true)
                    {
                        if (data.EndsWith("loopappend"))
                        {
                            Invoke(new MethodInvoker(delegate() { StartClient(data, 1234); }));
                            break;
                        }
                        else if (data == "shutdown")
                        {
                            shutdown++;
                            break;
                        }
                        else
                        {
                            break;
                        }
                    }

                    socket.Shutdown(SocketShutdown.Both);
                    socket.Close();
                }
            }
            catch (Exception e)
            {
                ExForm exForm = new ExForm();
                exForm.label1.Text = e.Message;
                exForm.ShowDialog();
            }
        }

        public void StartClient(string lel, int port)
        {
            byte[] bytes = new byte[1024];
            try
            {
                // Connect to a Remote server
                // Get Host IP Address that is used to establish a connection
                // In this case, we get one IP address of localhost that is IP : 127.0.0.1
                // If a host has multiple addresses, you will get a list of addresses
                IPHostEntry host = Dns.GetHostEntry("localhost");
                IPAddress ipAddress = host.AddressList[1];
                IPEndPoint remoteEP = new IPEndPoint(ipAddress, port);

                // Create a TCP/IP  socket.
                Socket sender = new Socket(ipAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp);

                // Connect the socket to the remote endpoint. Catch any errors.
                try
                {
                    // Connect to Remote EndPoint
                    sender.Connect(remoteEP);

                    msg = Encoding.ASCII.GetBytes(lel);

                    // Send the data through the socket.
                    int bytesSent = sender.Send(msg);

                    if (lel == "recon" || lel == "spedup" || lel == "speddown")
                    {
                        // Receive the response from the remote device.
                        int bytesRec = sender.Receive(bytes);


                        ptsd = Encoding.ASCII.GetString(bytes, 0, bytesRec);
                        label1.Text = "Speed: " + ptsd;
                    }
                    else if (lel == "colordef")
                    {
                        // Receive the response from the remote device.
                        int bytesRec = sender.Receive(bytes);

                        colony = Encoding.ASCII.GetString(bytes, 0, bytesRec);

                        if (colony.EndsWith("ENDERROR"))
                        {
                            shit++;
                            stifa = colony.Replace("ENDERROR", "");
                            ExForm fail = new ExForm();
                            fail.label1.Text = stifa;
                            fail.label1.ForeColor = Color.Red;
                            fail.ShowDialog();
                        }
                    }
                    else if (lel == "enumerate")
                    {
                        int bytesRec = sender.Receive(bytes);

                        numlol = Encoding.ASCII.GetString(bytes, 0, bytesRec);

                        enume = Convert.ToInt32(numlol);
                    }
                    else if (lel.EndsWith("getlist"))
                    {
                        int bytesRec = sender.Receive(bytes);

                        changed = Encoding.ASCII.GetString(bytes, 0, bytesRec);

                        listBox1.Items.Add(changed);
                    }
                    else if (lel.EndsWith("custom"))
                    {
                        int bytesRec = sender.Receive(bytes);

                        excheck = Encoding.ASCII.GetString(bytes, 0, bytesRec);
                        if (excheck == "WTF")
                        {
                            ExForm WTF = new ExForm();
                            WTF.label1.Text = "Invalid hex or color name, please try again";
                            WTF.label1.ForeColor = Color.Red;
                            WTF.ShowDialog();
                        }
                        else
                        {
                            enume = 7;
                            if (listBox1.Items.Count > enume - 1)
                            {
                                listBox1.Items.Remove(lmfo);
                            }
                            lmfo = excheck.Replace("7 ", "").Replace(" OK", "");
                            listBox1.Items.Add(lmfo);
                        }
                    }
                    else if (lel.EndsWith("loopbase") || lel.EndsWith("loopappend"))
                    {
                        LoopDef loopDef = new LoopDef();
                        if (lel.EndsWith("loopbase"))
                        {
                            lass = lmap;
                            loopDef.label1.Text = "Enter in " + lass + " more colors:";
                            loopDef.Show();
                        }

                        else if (lel.EndsWith("loopappend"))
                        {
                            int bytesRec = sender.Receive(bytes);

                            nowhere = Encoding.ASCII.GetString(bytes, 0, bytesRec);
                            if (nowhere == "DONE")
                            {
                                AddLooping();
                                AddToList(); 
                                loopss++;
                                this.button11.Location = new Point(35, 70);
                            }
                            else if (nowhere == "WTF")
                            {
                                ExForm exForm = new ExForm();
                                exForm.label1.Text = "Invalid loop color on one of specified colors, please try again";
                                exForm.label1.ForeColor = Color.Red;
                                exForm.ShowDialog();
                            }
                            else
                            {
                                lass--;
                                if (lass == 1)
                                {
                                    loopDef.label1.Text = "Enter in 1 more color:";
                                }
                                else
                                {
                                    loopDef.label1.Text = "Enter in " + lass + " more colors:";
                                }
                                loopDef.Show();
                            }
                        }
                    }
                    else if (lel == "red")
                    {
                        int bytesRec = sender.Receive(bytes);

                        R = Convert.ToInt32(Encoding.ASCII.GetString(bytes, 0, bytesRec));

                    }
                    else if (lel == "green")
                    {
                        int bytesRec = sender.Receive(bytes);

                        G = Convert.ToInt32(Encoding.ASCII.GetString(bytes, 0, bytesRec));
                    }
                    else if (lel == "blue")
                    {
                        int bytesRec = sender.Receive(bytes);

                        B = Convert.ToInt32(Encoding.ASCII.GetString(bytes, 0, bytesRec));
                    }
                    if (lel == "goup" || lel == "godown" || lel == "recon" || lel.EndsWith("change") || lel.EndsWith("loopappend") && (nowhere == "DONE" && nowhere != "WTF") || lel.EndsWith("custom"))
                    {
                        StartClient("red", 1234);
                        StartClient("green", 1234);
                        StartClient("blue", 1234);
                        button9.ForeColor = Color.FromArgb(R, G, B);
                    }
                    // Release the socket.
                    sender.Shutdown(SocketShutdown.Both);

                    sender.Close();
                }
                catch (ArgumentNullException ane)
                {
                    ExForm exForm = new ExForm();
                    exForm.label1.Text = $"ArgumentNullException : {ane.Message}";
                    exForm.ShowDialog();
                }
                catch (SocketException se)
                {
                    ExForm exForm = new ExForm();
                    exForm.label1.Text = $"SocketException : {se.Message}";
                    exForm.ShowDialog();
                }
                catch (Exception e)
                {
                    ExForm exForm = new ExForm();
                    exForm.label1.Text = $"Unexpected exception : {e.Message + " " + R + " " + G + " " + B}";
                    exForm.ShowDialog();
                }
            }
            catch (Exception e)
            {
                ExForm exForm = new ExForm();
                exForm.label1.Text = e.Message;
                exForm.ShowDialog();
            }
        }

        private void AddToList()
        {
            StartClient("enumerate", 1234);
            if (listBox1.Items.Count > 0)
            {
                listBox1.Items.Clear();
            }
            for (int i = 0; i < enume; i++)
            {
                StartClient(i.ToString() + " " + "getlist", 1234);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            StartClient("goup", 1234);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            StartClient("godown", 1234);
        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            Program.choice++;
            StartClient("quit", 1234);
            StartClient("shutdown", 5555);
            Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            StartClient("spedup", 1234);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            StartClient("speddown", 1234);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            StartClient("reverse", 1234);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            StartClient("lost", 1234);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            int lyght = Program.light;
            if (lyght == 0)
            {
                Program.light++;
                button7.Text = "Dark Theme";
            }
            else if (lyght == 1)
            {
                Program.light--;
                button7.Text = "Light Theme";
            }
            StartClient("light", 1234);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            StartClient("colordef", 1234);
            ColorForm colorForm = new ColorForm();
            colorForm.label1.Text = colony;
            if (shit == 1)
            {
                shit--;
            }
            else
            {
                if (loopss == 1)
                {
                    colorForm.label1.Location = new System.Drawing.Point(85, 76);
                }
                else { }
                colorForm.ShowDialog();
            }
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            wtshit = textBox1.Text;
        }

        private void textBox1_KeyUp(object sender, KeyPressEventArgs s)
	    {
	        if (s.KeyChar == (char) Keys.Enter)
            {
                Summon_Color();
            }
	    }

        private void Summon_Color()
        {
            string shti = wtshit + " custom";
            StartClient(shti, 1234);
            if (loopss == 1)
            {
                loopss--;
                RemoveLooping();
                AddToList();
            }
            textBox1.Text = "";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            Summon_Color();
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            chpk = listBox1.SelectedIndex;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            string indeed = chpk.ToString() + " change";
            StartClient(indeed, 1234);
        }

        private void button11_Click(object sender, EventArgs e)
        {
            askd = lmap.ToString() + " loopbase";
            StartClient(askd, 1234);
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            lmap = (int) numericUpDown1.Value;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            StartClient("endloop", 1234);
            loopss--;
            RemoveLooping();
            AddToList();
            StartClient("red", 1234);
            StartClient("green", 1234);
            StartClient("blue", 1234);
            button9.ForeColor = Color.FromArgb(R, G, B);
            this.button11.Location = new Point(626, 31);
        }

        private void button11_Click_1(object sender, EventArgs e)
        {
            Changelog changeds = new Changelog();
            changeds.Show();
        }
    }
}
