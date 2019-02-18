
fxs.append(
    {
        "name": "fdclean",
        "topic": "File descriptors",
        "info": "erases cached info about a file descriptor",
      
        "args": [
            {
                "name": "fd",
                "type": "int",
                "info": "file descriptor (OS-level one, not a libdill handle)"
            },
        ],

        "prologue": """
            This function drops any state that libdill associates with a file
            descriptor. It has to be called before the file descriptor is
            closed. If it is not, the behavior is undefined.

            It should also be used whenever you are losing control of the file
            descriptor. For example, when passing it to a third-party library.
            Also, if you are handed the file descriptor by third party code
            you should call this function just before returning it back to the
            original owner.
        """,

        "example": """
            int fds[2];
            pipe(fds);
            use_the_pipe(fds);
            fdclean(fds[0]);
            close(fds[0]);
            fdclean(fds[1]);
            close(fds[1]);
        """,
    }
)
