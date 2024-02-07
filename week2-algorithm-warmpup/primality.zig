const std = @import("std");

fn modPow(comptime T: type, b: T, e: T, mod: T) T {
    var result: T = 1;
    var base = b % mod;
    var exp = e;
    while (exp > 0) {
        if (exp & 1 == 1)
            result = (result * base) % mod;
        exp >>= 1;
        base = (base * base) % mod;
    }
    return result;
}

// fn random(comptime T: type) T {
//     var prng = std.rand.DefaultPrng.init(blck: {
//         var seed: u64 = undefined;
//         try std.os.getrandom(std.mem.asBytes((&seed)));
//         break :blck seed;
//     });
//     var size = @sizeOf(T);
//     var result: T = 0;
//     while (size > 0) {
//         var a = prng.random().int(u64);
//         result = (@as());
//     }
// }

// fn getRandomNumber(bits: u8) anyerror![]u8 {
//     var prng = std.rand.DefaultPrng.init(blck: {
//         var seed: u64 = undefined;
//         try std.os.getrandom(std.mem.asBytes((&seed)));
//         break :blck seed;
//     });

//     var bytes = bits / 8;
//     if (bits % 8 != 0) bytes += 1;

//     var result: []u8 = try std.mem.alloc(u8, bytes);
//     for (result) |*byte| {
//         byte.* = prng.random().int(u8);
//     }

//     return result;
// }

fn primality(n: u256) !bool {
    var prng = std.rand.DefaultPrng.init(blck: {
        var seed: u64 = undefined;
        try std.os.getrandom(std.mem.asBytes((&seed)));
        break :blck seed;
    });
    for (1..100) |_| {
        var a1 = prng.random().int(u64);
        var a2 = prng.random().int(u64);
        var a3 = prng.random().int(u64);
        var a4 = prng.random().int(u64);
        var aa = (@as(u128, a1) << 64) | @as(u128, a2);
        var ab = (@as(u128, a3) << 64) | @as(u128, a4);
        var a = (@as(u256, aa) << 128) | @as(u256, ab);
        a = a % (n - 2) + 1;
        if (modPow(u256, a, n - 1, n) != 1) {
            return false;
        }
    }
    return true;
}
fn genPrime() !u64 {
    var prng = std.rand.DefaultPrng.init(blck: {
        var seed: u64 = undefined;
        try std.os.getrandom(std.mem.asBytes((&seed)));
        break :blck seed;
    });
    // edge case of 0
    var result = prng.random().int(u64) + 1;
    while (!try primality(result)) {
        result = prng.random().int(u16);
    }
    return result;
}

pub fn main() !void {
    // var prime: u256 = std.math.pow(u256, 2, 3) - 1;
    var gprime = try genPrime();
    var isPrime = try primality(gprime);
    std.debug.print("gen prime: {}\n ", .{gprime});
    std.debug.print("is {} prime: {}\n", .{ gprime, isPrime });
}
