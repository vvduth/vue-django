export interface User {
  id: string;
  name: string;
  email: string;
  friends_count: number;
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
  };
}

export interface Friendrequest {
  id: string;
      created_by: User;
}

export interface GetFriendsResponse {
  data: {
    friends: User[];
    user: User;
    friendship_requests:Friendrequest[];
  };
}
