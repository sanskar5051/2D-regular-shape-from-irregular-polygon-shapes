#include <iostream>
using namespace std;

int main() 
{
  int answer=0;
  int num_ltrttb=0,num_ltrbtt=0,num_rtlttb=0,num_rtlbtt=0,num_ttbltr=0,num_ttbrtl=0,num_bttltr=0,num_bttrtl=0;
  int n,m;
  cin>>n>>m;
  int a,b;
  cin>>a>>b;
  int arr[a][b];
  for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            cin>>arr[i][j];
        }
    }
 
 // left to right traversal 
 
  //left to right top to bottom 
   int arr_ltrttb[a][b];
  for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            arr_ltrttb[i][j]=arr[i][j];
        }
    }
  for(int i=0;i<a;i++){
    for(int j=0;j<b;j++){
      int right_bottom_x=i+n-1;

      int right_bottom_y=j+m-1;
    
      int count=0;
      if(right_bottom_x < a && right_bottom_y < b){
      for(int k=i;k<=right_bottom_x;k++){
        for(int l=j;l<=right_bottom_y;l++){
          if(arr_ltrttb[k][l]==0){
            count=1;
          }
        }
      }
      if(count==0){
        cout<<"("<<i<<","<<j<<")-("<<right_bottom_x<<","<<right_bottom_y<<")"<<endl;
        num_ltrttb++;
        //converting found n*m box to 0
        for(int k=i;k<=right_bottom_x;k++){
        for(int l=j;l<=right_bottom_y;l++){
          arr_ltrttb[k][l]=0;
        }
      }
    
      }
    }
  }
  }
  if(num_ltrttb > answer){
    answer=num_ltrttb;
  }
  cout<<"number of n*m blocks in left to right and top to bottom traversal - "<<num_ltrttb<<endl;
  //end of left to right top to bottom 
  
  // left to right bottom to top 
  int arr_ltrbtt[a][b];
  for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            arr_ltrbtt[i][j]=arr[i][j];
        }
    }
  for(int i=a;i>=0;i--){
    for(int j=0;j<b;j++){
      int right_top_x=i-n+1;

      int right_top_y=j+m-1;
    
      int count=0;
      if(right_top_x >=0 && right_top_y < b){
      for(int k=right_top_x;k<=i;k++){
        for(int l=j;l<=right_top_y;l++){
          if(arr_ltrbtt[k][l]==0){
            count=1;
          }
        }
      }
      if(count==0){
        cout<<"("<<i<<","<<j<<")-("<<right_top_x<<","<<right_top_y<<")"<<endl;
        num_ltrbtt++;
        //converting found n*m box to 0
        for(int k=right_top_x;k<=i;k++){
        for(int l=j;l<=right_top_y;l++){
          arr_ltrbtt[k][l]=0;
        }
      }
    
      }
    }
  }
  }
  if(num_ltrbtt > answer){
    answer=num_ltrbtt;
  }
   cout<<"number of n*m blocks in left to right and bottom to top traversal - "<<num_ltrbtt<<endl;
   //end of left to right bottom to top 
   
   //right to left top to bottom 
    int arr_rtlttb[a][b];
  for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            arr_rtlttb[i][j]=arr[i][j];
        }
    }
  for(int i=0;i<a;i++){
    for(int j=b;j>=0;j--){
      int left_bottom_x=i+n-1;

      int left_bottom_y=j-m+1;
    
      int count=0;
      if(left_bottom_x < a && left_bottom_y >=0){
      for(int k=i;k<=left_bottom_x;k++){
        for(int l=left_bottom_y;l<=j;l++){
          if(arr_rtlttb[k][l]==0){
            count=1;
          }
        }
      }
      if(count==0){
        cout<<"("<<i<<","<<j<<")-("<<left_bottom_x<<","<<left_bottom_y<<")"<<endl;
        num_rtlttb++;
        //converting found n*m box to 0
        for(int k=i;k<=left_bottom_x;k++){
        for(int l=left_bottom_y;l<=j;l++){
          arr_rtlttb[k][l]=0;
        }
      }
    
      }
    }
  }
  }
  if(num_rtlttb > answer){
    answer=num_rtlttb;
  }
   cout<<"number of n*m blocks in right to left and top to bottom traversal - "<<num_rtlttb<<endl;
  // end of right to left top to bottom
  
  //right to left bottom to top 
   int arr_rtlbtt[a][b];
  for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            arr_rtlbtt[i][j]=arr[i][j];
        }
    }
  for(int i=a;i>=0;i--){
    for(int j=b;j>=0;j--){
      int left_top_x=i-n+1;

      int left_top_y=j-m+1;
    
      int count=0;
      if(left_top_x >=0 && left_top_y >=0){
      for(int k=left_top_x;k<=i;k++){
        for(int l=left_top_y;l<=j;l++){
          if(arr_rtlbtt[k][l]==0){
            count=1;
          }
        }
      }
      if(count==0){
        cout<<"("<<i<<","<<j<<")-("<<left_top_x<<","<<left_top_y<<")"<<endl;
        num_rtlbtt++;
        //converting found n*m box to 0
        for(int k=left_top_x;k<=i;k++){
        for(int l=left_top_y;l<=j;l++){
          arr_rtlbtt[k][l]=0;
        }
      }
    
      }
    }
  }
  }
  if(num_rtlbtt > answer){
    answer=num_rtlbtt;
  }
 cout<<"number of n*m blocks in right to left and bottom to top traversal - "<<num_rtlbtt<<endl;
  // end of right to left bottom to top 
  
  
  // top to bottom traversal
  
  // top to bottom left to right 
   int arr_ttbltr[a][b];
  for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            arr_ttbltr[i][j]=arr[i][j];
        }
    }
  for(int j=0;j<b;j++){
    for(int i=0;i<a;i++){
      int right_bottom_x=i+n-1;

      int right_bottom_y=j+m-1;
    
      int count=0;
      if(right_bottom_x < a && right_bottom_y < b){
        
     
        for(int l=j;l<=right_bottom_y;l++){
           for(int k=i;k<=right_bottom_x;k++){
          if(arr_ttbltr[k][l]==0){
            count=1;
          }
        }
      }
      if(count==0){
        cout<<"("<<i<<","<<j<<")-("<<right_bottom_x<<","<<right_bottom_y<<")"<<endl;
        num_ttbltr++;
        //converting found n*m box to 0
      
        for(int l=j;l<=right_bottom_y;l++){
          for(int k=i;k<=right_bottom_x;k++){
          arr_ttbltr[k][l]=0;
        }
      }
    
      }
    }
  }
  }
  if(num_ttbltr > answer){
    answer=num_ttbltr;
  }
   cout<<"number of n*m blocks in top to bottom and left to right traversal - "<<num_ttbltr<<endl;

  //end of top to bottom left to right 
  
  //top to bottom right to left 
  int arr_ttbrtl[a][b];
  for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            arr_ttbrtl[i][j]=arr[i][j];
        }
    }
  
    for(int j=b;j>=0;j--){
      for(int i=0;i<a;i++){
      int left_bottom_x=i+n-1;

      int left_bottom_y=j-m+1;
    
      int count=0;
      if(left_bottom_x < a && left_bottom_y >=0){
        for(int l=left_bottom_y;l<=j;l++){
          for(int k=i;k<=left_bottom_x;k++){
          if(arr_ttbrtl[k][l]==0){
            count=1;
          }
        }
      }
      if(count==0){
        cout<<"("<<i<<","<<j<<")-("<<left_bottom_x<<","<<left_bottom_y<<")"<<endl;
        num_ttbrtl++;
        //converting found n*m box to 0
        
        for(int l=left_bottom_y;l<=j;l++){
          for(int k=i;k<=left_bottom_x;k++){
          arr_ttbrtl[k][l]=0;
        }
      }
    
      }
    }
  }
  }
  if(num_ttbrtl > answer){
    answer=num_ttbrtl;
  }
   cout<<"number of n*m blocks in top to bottom and right to left traversal - "<<num_ttbrtl<<endl;
  //end of top to bottom right to left 
  
  //bottom to top left to right 
  int arr_bttltr[a][b];
  for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            arr_bttltr[i][j]=arr[i][j];
        }
    }
  
    for(int j=0;j<b;j++){
      for(int i=a;i>=0;i--){
      int right_top_x=i-n+1;

      int right_top_y=j+m-1;
    
      int count=0;
      if(right_top_x >=0 && right_top_y < b){
      
        for(int l=j;l<=right_top_y;l++){
          for(int k=right_top_x;k<=i;k++){
          if(arr_bttltr[k][l]==0){
            count=1;
          }
        }
      }
      if(count==0){
        cout<<"("<<i<<","<<j<<")-("<<right_top_x<<","<<right_top_y<<")"<<endl;
        num_bttltr++;
        //converting found n*m box to 0
        
        for(int l=j;l<=right_top_y;l++){
          for(int k=right_top_x;k<=i;k++){
          arr_bttltr[k][l]=0;
        }
      }
    
      }
    }
  }
  }
  if(num_bttltr > answer){
    answer=num_bttltr;
  }
   cout<<"number of n*m blocks in bottom to top and left to right traversal - "<<num_bttltr<<endl;
  // end of bottom to top left to right 
  
  // bottom to top right to left 
   int arr_bttrtl[a][b];
  for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            arr_bttrtl[i][j]=arr[i][j];
        }
    }
  
    for(int j=b;j>=0;j--){
      for(int i=a;i>=0;i--){
      int left_top_x=i-n+1;

      int left_top_y=j-m+1;
    
      int count=0;
      if(left_top_x >=0 && left_top_y >=0){
      
        for(int l=left_top_y;l<=j;l++){
          for(int k=left_top_x;k<=i;k++){
          if(arr_bttrtl[k][l]==0){
            count=1;
          }
        }
      }
      if(count==0){
        cout<<"("<<i<<","<<j<<")-("<<left_top_x<<","<<left_top_y<<")"<<endl;
        num_bttrtl++;
        //converting found n*m box to 0
        
        for(int l=left_top_y;l<=j;l++){
          for(int k=left_top_x;k<=i;k++){
          arr_bttrtl[k][l]=0;
        }
      }
    
      }
    }
  }
  }
  if(num_bttrtl > answer){
    answer=num_bttrtl;
  }
   cout<<"number of n*m blocks in bottom to top and right to left traversal - "<<num_bttrtl<<endl;
  // ond of bottom to top right to left 
  
  
  // final answer 
  cout << "total number of n*m block in the above settelment with maximum space occupency is "<<answer;
  
    return 0;
}
