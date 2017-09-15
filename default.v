module default #(
parameter	COUNTWID	=	16,
parameter	RADIUS	=	10,
parameter	RESULTWID	=	15,
parameter	WEIGHT	=	3)
(input	wire	[0:0]	clk,
input	wire	[0:0]	phaseA_rise,
input	wire	[0:0]	rst_n,
output	reg	[14:0]	result);
localparam	CALCWID	=	32;
localparam	TIMESWID	=	2;


reg	[15:0]	counter;
reg	[2:0]	times;




endmodule