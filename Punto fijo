#include <math.h>
#include <stdio.h>
#include <stdlib.h>

/* funciones  */
double G( double );
double getError( double , double );
double abs_val( double );

int main( int argc , char ** argv )
{
    double P = 0, Pant = 0, a = 0, b = 0;
	int n = 0, e = 0;
	if ( argc != 5 )
	{
		printf ( "%s", "\n\n Error: Not enough arguments supplied \n  ->Usage: ./biseccion limit_a limit_b Pant exp_epsilon \n\n" );
		return 1;
	}
	else
	{			
		//a = atof( argv[1] );
		//b = atof( argv[2] );
		Pant = atof( argv[3] );
		e = atoi( argv[4] );
		P = G( Pant );
		printf("\n\n");
		n++;
		while(getError(P,  Pant) > pow(10,e))
		{
			printf("\n %d - %.9f - %.9f - %.9f ",n, P, Pant, getError(P, Pant));
			Pant = P;
			P = G(Pant);
			n++;
		}
		printf("\n\n RESULTADO: %.9f \n\n",P);
	}
	return 0;	
}

/* definicion de funciones */

/* funcion G(x) */
double G( double x )
{
	return pow( ( ( 3 * pow(x,2) ) + 3 ), 0.25 );
}

/* devuelve el error */
double getError( double P, double Pant )
{
	return abs_val( P - Pant );
}

/* devuelve valor absoluto de un numero */
double abs_val( double a )
{
	if ( a < 0 )
	{
		return -1 * a;
	}
	else
	{
		return a;
	}
}
