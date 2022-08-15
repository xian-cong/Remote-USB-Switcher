using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO.Ports;

namespace Switcher
{
    public partial class Form1 : Form
    {
        private SerialPort myport;
        public Form1()
        {
            InitializeComponent();
            init();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            myport.WriteLine("s");
            button1.Enabled = false;
        }

        private void init()
        {
            try
            {
                myport = new SerialPort();
                myport.BaudRate = 9600;
                myport.PortName = "COM6";
                myport.Open();

                button1.Enabled = true;
            }
            catch(Exception)
            {
                MessageBox.Show("Error!");
            }
        }
    }
}
