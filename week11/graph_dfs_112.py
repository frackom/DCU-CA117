#!/usr/bin/env python3

class Graph(object):
   def __init__(self, V):
      self.V = V
      self.adj = {}
      for v in range(V):
         self.adj[v] = []

   def addEdge(self, v, w):
      self.adj[v].append(w)
      self.adj[w].append(v)

   def degree(self, v):
      return len(self.adj[v])

   def maxDegree(self):
      return max([len(self.adj[v]) for v in range(self.V)])

   def avgDegree(self):
      return sum([self.degree(v) for v in range(self.V)]) / self.V

class DFSPaths(object):
   def __init__(self, g, s):
      self.g = g
      self.s = s

      self.visited = [False] * g.V
      self.parent = [-1] * g.V
      self.dfs(s)

   def dfs(self, v):
      self.visited[v] = True
      for w in self.g.adj[v]:
         if not self.visited[w]:
            self.parent[w] = v
            self.dfs(w)

   def hasPathTo(self, v):
      return self.visited[v]

   def pathTo(self, v):
      if not self.hasPathTo(v):
         return []
      path = [v]
      while v != self.s:
         v = self.parent[v]
         path.append(v)
      return path[::-1]
