#include <lcd.h>

int main(void)
{
	int i;
	int fd;
	fd = lcdInit(2,16,4,15,16, 0,1,2,3,4,5,6,7);
	lcdPosition(fd,0,0);
	lcdPuts(fd,"Hola");
	}
