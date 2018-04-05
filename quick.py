int partition(int v[], int l, int r) {
    int temp;
    int p = l;
    for(int i = l; i < r; i++) {
        if(v[i] < v[r]) {
            temp = v[p];
            v[p] = v[i];
            v[i] = temp;
            p++;
        }
      }
    temp = v[p];
    v[p] = v[r];
    v[r] = temp;
    return p;
}

void quick_sort_r(int v[], int l, int r) {
    if(l >= r) {
    return;
    }
    int p = partition(v, l, r);
    quick_sort_r(v, l, p - 1);
    quick_sort_r(v, p + 1, r);
}



