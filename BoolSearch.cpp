int bisect_right(int l,int r,bool (*pf)(int)){
    /*
    查找右侧第一个True
    对于一个形如[False...False,True...True]的序列
    此方法用于获取右侧第一个True的下标
    [l,r]是查找范围
    pf是一个函数，返回指定坐标x的布尔值
    */
    while(l<r){
        int mid = (l+r)/2;
        if((*pf)(mid))
            r=mid;
        else 
            l=mid+1;
        }
    return r;
}

int bisect_left(int l,int r,bool (*pf)(int)){
    /*
    查找左侧最后一个True
    对于一个形如[True...True,False...False]的序列
    此方法用于获取左侧最后一个True的下标
    [l,r]是查找范围
    pf是一个函数，返回指定坐标x的布尔值
    */
    while(l<r){
        int mid=(l+r)/2+1;
        if((*pf)(mid))
            l=mid;
        else
            r=mid-1;
    }
    return l;
}