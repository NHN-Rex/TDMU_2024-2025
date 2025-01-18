# import networkx as nx
# import matplotlib
# edges = []
# f = open('twitter_followings.txt', 'r')
# for line in f.readlines():
#     id1, id2 = line.strip().split()
#     edges.append((id1,id2))
# # create directed graph from the edge pairs using NetworkX Library
# G = nx.DiGraph(edges)
# # visualize the graph
# nx.draw(G, with_labels=True, arrows=True, arrowstyle='-|>', arrowsize=15,
#         node_color='#3498DB', node_size=800, 
#         edge_color='#FF5733')
# mutual_followers = []
# # Xét tất cả các cạnh trên đồ thị
# for u, v in G.edges():
#     # Nếu có kết nối u->v và v->u thì (u,v) là cặp theo dõi lẫn nhau
#     if G.has_edge(u,v) and G.has_edge(v,u):
#         # Tránh việc liệt kê 1 cặp tài khoản 2 lần
#         if (v, u) not in mutual_followers:
#             mutual_followers.append((u, v))
# # List mutual follower pairs:
# print('Các cặp tài khoản theo dõi lẫn nhau:')
# for u, v in mutual_followers:
#     print(u, '<->', v)


import networkx as nx
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file và tạo danh sách các cạnh
edges = []
with open('twitter_followings.txt', 'r') as f:
    for line in f:
        id1, id2 = line.strip().split()
        edges.append((id1, id2))

# Tạo đồ thị có hướng từ danh sách các cạnh
G = nx.DiGraph(edges)

# Tìm mutual followers
mutual_followers = []
for u, v in G.edges():
    if G.has_edge(v, u):
        if (v, u) not in mutual_followers:
            mutual_followers.append((u, v))

# In các cặp mutual followers
print('Các cặp tài khoản theo dõi lẫn nhau:')
for u, v in mutual_followers:
    print(f'{u} <-> {v}')

# **Bổ sung 1: Thiết lập vị trí các node để đồ thị đẹp hơn**
pos = nx.spring_layout(G, k=0.15, iterations=20)

# **Bổ sung 2: Vẽ tất cả các cạnh không phải mutual followers**
non_mutual_edges = [edge for edge in G.edges() if edge not in mutual_followers and (edge[1], edge[0]) not in mutual_followers]
nx.draw_networkx_nodes(G, pos, node_size=800, node_color='#3498DB')
nx.draw_networkx_labels(G, pos, font_size=12, font_color='white')

# Vẽ các cạnh không phải mutual followers
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=non_mutual_edges,
    edge_color='#FF5733',
    arrows=True,
    arrowstyle='-|>',
    arrowsize=15,
    label='Following'
)

# **Bổ sung 3: Vẽ các cạnh mutual followers với màu khác**
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=mutual_followers,
    edge_color='green',
    arrows=True,
    arrowstyle='-|>',
    arrowsize=15,
    label='Mutual Following',
    connectionstyle='arc3, rad=0.1'  # Để tránh các cạnh chồng lắp
)

# **Bổ sung 4: Tạo legend cho đồ thị**
import matplotlib.patches as mpatches

following_patch = mpatches.Patch(color='#FF5733', label='Following')
mutual_patch = mpatches.Patch(color='green', label='Mutual Following')
plt.legend(handles=[following_patch, mutual_patch])

# **Bổ sung 5: Tùy chỉnh hiển thị đồ thị**
plt.title('Twitter Followers Graph')
plt.axis('off')  # Tắt hiển thị trục
plt.tight_layout()

# **Bổ sung 6: Hiển thị đồ thị**
plt.show()

# **Tùy chọn: Lưu đồ thị vào file hình ảnh**
# plt.savefig('twitter_followers_graph.png', format='PNG')
