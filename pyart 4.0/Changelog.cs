using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;
using System.Windows.Forms;

namespace pyart_4._0
{
    public partial class Changelog : Form
    {
        public Changelog()
        {
            InitializeComponent();
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            using (Process wtflolsd = new Process())
            {
                wtflolsd.StartInfo.FileName = "https://drive.google.com/drive/folders/1yb-VcgXpkmF9ULQyUolACCkNuEoNAzpO?usp=sharing";
                wtflolsd.StartInfo.UseShellExecute = true;
                linkLabel1.LinkVisited = true;
                wtflolsd.Start();

                wtflolsd.WaitForExit();
            }
        }
    }
}
