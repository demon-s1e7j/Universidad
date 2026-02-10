A = [0 1 0 0; 0 0 2 0; 0 0 0 3; 0 0 0 0];

[V, D] = eig(A);

disp('Eigenvector matrix V:');
disp(V);

disp('Rank of V:');
disp(rank(V));

if rank(V) < length(A)
    disp('Matrix is not diagonalizable.');
end
