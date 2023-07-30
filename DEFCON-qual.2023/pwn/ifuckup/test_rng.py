class Random:
    def __init__(self, seed):
        self.rand_tab = seed
        self.i = 0

    def next_rand(self):
        i = self.i

        ni = (i + 0xf) % 0x10
        rval_1 = self.rand_tab[(i + 0xd) % 0x10]
        rval_2 = self.rand_tab[ni]
        rval_3 = self.rand_tab[(i + 0x9) % 0x10]
    
        tmp1 = (self.rand_tab[i] << 0x10 ^ self.rand_tab[i] ^ rval_1 ^ rval_1 \
                << 0xf) % 2**32
        tmp2 = rval_3 >> 0xb ^ rval_3
    
        new_rng_i = tmp1 ^ tmp2
        new_rng_ni = (tmp1 << 0x12 ^ rval_2 << 2 ^ rval_2 ^ tmp2 ^ tmp2 << \
                0x1c ^ (new_rng_i << 5 & 0xda442d24)) % 2 ** 32
    
        self.rand_tab[i] = new_rng_i
        self.rand_tab[ni] = new_rng_ni

        self.i = ni
    
        return new_rng_ni

rand = Random([
	0xc0cb97ba,0xec02f853,0x1fdb8329
,0x2e874fc7,0x0dedf8cd,0xf20c0b20,0x2280cb9b
,0xe62f20f7,0x3c5dfcf9,0xcd1f1ca3,0x528108ec
,0x4ce89ffa,0x04056ec2,0xb9fa6297,0x26659a91
,0x217dd72e
    ])

for i in range(2):
    print( hex(rand.next_rand()))
    for i in rand.rand_tab:
        print(hex(i))
    print("\n\n\n\n")
    # print(hex(int(rand.next_rand())))# * c_float(2.32830644e-10).value *
                  #4294967295.0)))