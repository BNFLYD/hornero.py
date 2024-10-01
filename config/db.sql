CREATE TABLE users (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    is_verified BOOLEAN DEFAULT false,
    is_public BOOLEAN DEFAULT true
);
CREATE TABLE follows (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    follower_id BIGINT REFERENCES users(id),
    followed_id BIGINT REFERENCES users(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    is_approved BOOLEAN DEFAULT false
);
CREATE TABLE blocks (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    blocker_id BIGINT REFERENCES users(id),
    blocked_id BIGINT REFERENCES users(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);
CREATE TABLE posts (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id BIGINT REFERENCES users(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    markdown_content TEXT,
    parent_post_id BIGINT REFERENCES posts(id)
);
CREATE TABLE comments (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id BIGINT REFERENCES users(id),
    post_id BIGINT REFERENCES posts(id),
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);
CREATE TABLE media (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    media_url TEXT NOT NULL,
    media_type TEXT CHECK (media_type = ANY (ARRAY['image', 'video'])),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    content_type TEXT NOT NULL,
    content_id BIGINT NOT NULL,
    post_id BIGINT REFERENCES posts(id) ON DELETE CASCADE,
    comment_id BIGINT REFERENCES comments(id) ON DELETE CASCADE
);
CREATE TABLE reposts (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id BIGINT REFERENCES users(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    content_type TEXT NOT NULL,
    content_id BIGINT NOT NULL
);
CREATE TABLE likes (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id BIGINT REFERENCES users(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    content_type TEXT NOT NULL,
    content_id BIGINT NOT NULL
);
CREATE TABLE links (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    post_id BIGINT REFERENCES posts(id),
    url TEXT NOT NULL,
    title TEXT,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);
CREATE TABLE lists (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id BIGINT REFERENCES users(id),
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);
CREATE TABLE list_members (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    list_id BIGINT REFERENCES lists(id),
    member_id BIGINT REFERENCES users(id),
    added_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);
CREATE TABLE trends (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    hashtag TEXT NOT NULL,
    post_count BIGINT DEFAULT 0,
    last_updated TIMESTAMP WITH TIME ZONE DEFAULT now()
);
CREATE TABLE messages (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    sender_id BIGINT REFERENCES users(id),
    receiver_id BIGINT REFERENCES users(id),
    content TEXT,
    media_url TEXT,
    media_type TEXT CHECK (media_type = ANY (ARRAY['image', 'video', 'audio', 'text'])),
    sent_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    is_read BOOLEAN DEFAULT false
);
CREATE TABLE message_requests (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    sender_id BIGINT REFERENCES users(id),
    receiver_id BIGINT REFERENCES users(id),
    is_approved BOOLEAN DEFAULT false
);