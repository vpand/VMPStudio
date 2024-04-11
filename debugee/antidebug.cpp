#include <unistd.h>
#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#if __APPLE__
#include <sys/types.h>
#include <sys/sysctl.h>

typedef int (*ptrace_ptr_t)(int _request, pid_t _pid, caddr_t _addr, int _data);

static void anti_debug() {
  ptrace_ptr_t ptrace_ptr = (ptrace_ptr_t)dlsym(RTLD_SELF, "ptrace");
  if (!ptrace_ptr) {
    printf("Failed to get ptrace symbol address.\n");
    return;
  }
  ptrace_ptr(31, 0, 0, 0); // PTRACE_DENY_ATTACH = 31
}

// Returns true if the current process is being debugged (either
// running under the debugger or has a debugger attached post facto).
static bool am_I_being_debugged(void) {
  int                 junk;
  int                 mib[4];
  struct kinfo_proc   info;
  size_t              size;

  // Initialize the flags so that, if sysctl fails for some bizarre
  // reason, we get a predictable result.
  info.kp_proc.p_flag = 0;

  // Initialize mib, which tells sysctl the info we want, in this case
  // we're looking for information about a specific process ID.
  mib[0] = CTL_KERN;
  mib[1] = KERN_PROC;
  mib[2] = KERN_PROC_PID;
  mib[3] = getpid();

  // Call sysctl.
  size = sizeof(info);
  sysctl(mib, sizeof(mib) / sizeof(*mib), &info, &size, NULL, 0);
  // We're being debugged if the P_TRACED flag is set.
  if ((info.kp_proc.p_flag & P_TRACED) != 0) {
    printf("p_flag is %x.\n", info.kp_proc.p_flag);
    return true;
  }
  else {
    printf("not P_TRACED.\n");
    return false;
  }
}
#else
static void anti_debug() {}

// Returns true if the current process is being debugged (either
// running under the debugger or has a debugger attached post facto).
static bool am_I_being_debugged(void) {
  FILE *fp = fopen("/proc/self/status", "r");
  char status[128];
  size_t rd = fread(status, 1, sizeof(status) - 1, fp);
  status[rd] = 0;
  fclose(fp);
  return strstr(status, "TracerPid:\t0") == nullptr;
}
#endif

void do_main(int argc, const char *argv[]) {
  if (!getenv("NO_ANTIDBG")) {
    anti_debug();
  }

  for (int i = 0; i < argc; i++) {
    bool dbg = am_I_being_debugged();
    printf(
      "Running %s, I'm being debugged(%s).\n", 
      argv[0],
      dbg ? "true" : "false");

    if (dbg) {
      // infinity loop if under control
      i = 0;
    }
    sleep(2);
  }

  // what a nice day...
  puts("Have fun with UraniumVM Studio~");  
}

int main(int argc, const char *argv[]) {
  printf("Input 'q' to quit and 'r' to run the ollvm main entry.\n");
  while (true) {
    char ch = getchar();
    if (ch == 'q') break;
    if (ch == 'r') do_main(argc, argv);
  }
  return 0;
}
