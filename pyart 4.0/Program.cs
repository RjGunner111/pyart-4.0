using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Diagnostics;
using System.Net;
using System.Net.Sockets;
using System.Threading;
using System.Text;
using System.Windows.Forms;
using System.IO;

namespace pyart_4._0
{
    internal class Program
    {
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            choice = 0;
            light = 0;
            Application.SetHighDpiMode(HighDpiMode.SystemAware);
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Program program = new Program();
            program.ProgramMain();
            Application.Run(new Form1());
            if (choice == 0)
            {
                Done();
            }
        }

        public static string? script;

        public static int choice;

        public static int light;

        public void ProgramMain()
        {
            var psi = new ProcessStartInfo();
            psi.FileName = @"C:\Program Files\Python3\python.exe";

            string? folder = Path.GetDirectoryName(Process.GetCurrentProcess().MainModule.FileName);
            string newPath = Path.GetFullPath(Path.Combine(folder, @"..\..\..\"));

            script = $@"{newPath}pyart 4.0.py";
            psi.Arguments = $"\"{script}\"";

            // 3) Process configuration
            psi.UseShellExecute = false;
            psi.CreateNoWindow = true;

            Process.Start(psi);
        }

        static void Done()
        {
            Form1 form1 = new Form1();
            form1.shutdown++;
            form1.StartClient("quit", 1234);
            form1.StartClient("shutdown", 5555);
        }
    }
}