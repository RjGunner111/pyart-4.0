using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.Windows.Forms;
using System.Net;
using System.Net.Sockets;

namespace pyart_4._0
{
    public partial class LoopDef : Form
    {
        public LoopDef()
        {
            InitializeComponent();
        }

        public string nope;
        public int wtfprevent;
        private byte[] msg;

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            nope = textBox1.Text;
        }

        private void textBox1_KeyUp(object sender, KeyPressEventArgs s)
        {
            if (s.KeyChar == (char)Keys.Enter)
            {
                Close();
                StartClient(nope + " loopappend");
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Close();
            StartClient(nope + " loopappend");
        }
        public void StartClient(string lel)
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
                IPEndPoint remoteEP = new IPEndPoint(ipAddress, 5555);

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
                    exForm.label1.Text = $"Unexpected exception : {e.Message}";
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
    }
}
