using Combinatorics

I = [ 1 0; 0 1]
X = [0 1; 1 0]
Z = [1 0; 0 -1]
XZ = X * Z

function innerProduct(A, B)
end

base = Dict("I" => I, "X" => X, "Z" => Z, "XZ" => XZ)

combs_iter = combinations(keys(base), 2)


