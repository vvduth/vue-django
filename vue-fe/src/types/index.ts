export interface User {
  id: string;
  name: string;
  email: string;
}

export interface Post {
  id: number;
  body: string;
  created_by: {
    id: string;
    name: string;
    email: string;
  };
  created_at_formatted: string;
}

export interface SerachResponse {
  data: {
    posts: Post[];
  users: User[];
  }
  
}