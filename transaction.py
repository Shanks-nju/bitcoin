from bitcoin import *


def tx(frm, to_, value_, fee_=10000, **kwargs):
    return multi_tx(frm, to_ + ":" + str(value_), fee_, **kwargs)


def multi_tx(frm, *args, **kwargs):
    tv, fee_ = args[:-1], int(args[-1])
    outs = []
    out_value = 0
    for a in tv:
        outs.append(a)
        out_value += int(a.split(":")[1])

    u = unspent(frm, **kwargs)
    u2 = select(u, int(out_value) + int(fee_))
    argz = u2 + outs + [frm, fee_]
    tst = mksend(*argz)
    return tst


fm = raw_input('from address: ')
to = raw_input('to address: ')
value = raw_input('btc num: ')
fee_str = raw_input('fee: ')

fee = int(fee_str)

print tx(fm, to, 10000, fee)
