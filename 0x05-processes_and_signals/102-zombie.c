#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
* infinite_while - infinite
* Return: 0
*/

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - Entry point
 * Return: creates 5 zombie processes.
 */
int main(void)
{
	pid_t pid;
	int i;

	while (i < 5)
	{
		pid = fork();
		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		i++;
	}
	return (infinite_while());
}
