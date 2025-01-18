def pagerank(pages, links, iterations=10, d=0.85):
    n = len(pages)
    pr = {page: 1/n for page in pages}
    for _ in range(iterations):
        new_pr = {}
        for page in pages:
            new_pr[page] = (1 - d) / n + d * sum(pr[link] / len(links[link]) for link in links if page in links[link])
        print(pr)
        pr = new_pr
    # return pr

pages = ['A', 'B', 'C', 'D']
links = {
    'B': ['A', 'C'],
    'C': ['A'],
    'D': ['A', 'B', 'C']
}

pr_values = pagerank(pages, links)
# print(pr_values)