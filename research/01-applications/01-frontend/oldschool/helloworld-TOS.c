#include <aesbind.h>
#include <vdibind.h>

int main()
{
    int handle;
    int msg_buf[8];

    handle = appl_init();
    if (handle <= 0) {
        printf("Failed to initialize AES!\n");
        return 1;
    }

    appl_write_string("Hello, World!", 1, 1, 1);

    form_alert(1, "Hello");

    while (1) {
        evnt_mesag(msg_buf);
        if (msg_buf[0] == AC_CLOSE) {
            break;
        }
    }

    appl_exit();

    return 0;
}
