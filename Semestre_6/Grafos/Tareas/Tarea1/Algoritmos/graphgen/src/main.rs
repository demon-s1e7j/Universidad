fn graphgen(lista: Vec<usize>) -> (bool, Vec<usize>) {
    let n = lista.len();
    let mut lista_nueva = lista.clone();
    let mut adj = vec![vec![0; n];n];
    let mut i = 0;
    while i < n && lista_nueva[i] > 0 {
        let k = lista_nueva[i];
        if i+k <= n && lista_nueva[i+k] > 0 {
            for j in n-k..n {
                adj[i][j] = 1;
                adj[j][i] = 1;
                lista_nueva[j] -= 1;
            }
        }
        println!("{:?}",adj);
        lista_nueva[i] = 0;
        i += 1;
    }
    return (true, vec![0,0]);
}

fn main() {
    graphgen(vec![3,3,3,3]);
}
