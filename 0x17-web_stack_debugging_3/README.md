# 0x17. Web stack debugging #3
## strace 
is a diagnostic, debugging and instructional userspace utility for Linux. It is used to monitor and tamper with interactions between processes and the Linux kernel, which include system calls, signal deliveries, and changes of process state.

System administrators, diagnosticians and trouble-shooters will find it invaluable for solving problems with programs for which the source is not readily available since they do not need to be recompiled in order to trace them.

The operation of strace is made possible by the kernel feature known as ptrace.
NAME         top

       strace - trace system calls and signals

SYNOPSIS         top

       strace [-ACdffhikqqrtttTvVwxxyyzZ] [-I n] [-b execve] [-e expr]...
              [-O overhead] [-S sortby] [-U columns] [-a column] [-o file]
              [-s strsize] [-X format] [-P path]... [-p pid]...
              [--seccomp-bpf] { -p pid | [-DDD] [-E var[=val]]...
              [-u username] command [args] }

       strace -c [-dfwzZ] [-I n] [-b execve] [-e expr]... [-O overhead]
              [-S sortby] [-U columns] [-P path]... [-p pid]...
              [--seccomp-bpf] { -p pid | [-DDD] [-E var[=val]]...
              [-u username] command [args] }

------------------------------------------------------------------------------------
#used
--> strace -p 
--> ps auxf : 
The ps (process status) command is one of the most frequently used commands in Linux. Usually it is used to get the more and detailed information about a specific process or all processes. For example it is used to know whether a particular process is running or not, who is running what process in system, which process is using higher memory or CPU, how long a process is running, etc.
 * To see every process on the system using BSD syntax:
          ps ax
          ps axu
