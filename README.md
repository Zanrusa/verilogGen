A verilog HDL code generator.Generate a verilog module in the form below is possible.It can also analyse a single module in a .v file and classify basic element inside the module,such as parameter,input,output,wire,et al.Use pyqt5 UI structure in this project. 

        module maincha #(
        parameter	EXCUSE_ME	=	250,
        parameter	WTF	=	100)
        (input	wire	[1:0]	b,
        input	wire	[1:0]	uasd,
        input	wire	[0:0]	c,
        input	wire	[3:0]	uhel,
        input	wire	[1:0]	spi_miso,
        input	wire	[9:0]	uart_data,
        input	wire	[0:0]	uart_rx,
        input	wire	[6:0]	sa,
        input	wire	[0:0]	a,
        output	reg	[0:0]	uart_clk,
        output	reg	[1:0]	spi_mosi,
        output	reg	[1:0]	spi_clk,
        output	reg	[1:0]	spi_cs,
        output	reg	[8:0]	reg_out,
        output	reg	[0:0]	uart_tx,
        output	wire	[8:0]	wire_out);
        localparam	WID_OF_MINE	=	8;

        wire	[10:0]	bus_intofile;

        reg	[5:0]	data_count;

        endmodule

