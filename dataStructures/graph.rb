require_relative 'queue'
require_relative 'stack'

class Graph
  attr_accessor :vertices

  def initialize
    @order = 0
    @vertices = {}
  end

  def get_vertex(key)
    return @vertices[key]
  end

  def add_vertex(key)
    @order += 0
    vertex = Vertex.new(key)
    @vertices[key] = vertex
  end

  def add_edge(fromKey, toKey)
    src = @vertices[fromKey]
    dst = @vertices[toKey]
    src.add_neighbour(dst)
    dst.add_neighbour(src)
  end

  def print_graph
    @vertices.each do |_,vert|
      puts vert
    end
  end

end

class DiGraph < Graph

  def add_edge(fromKey, toKey)
    src = @vertices[fromKey]
    dst = @vertices[toKey]
    src.add_neighbour(dst)
  end

end

class Vertex
  attr_accessor :key, :neighbours

  def initialize(key)
    @key = key
    @neighbours = {}
  end

  def add_neighbour(nbr, weight=0)
    @neighbours[nbr] = weight
  end

  def to_s
    str = ""
    @neighbours.each do |nbr,_|
      str += "(" + @key + "," + nbr.key + ") "
    end
    return str
  end

end


class AdjMatrixGraph

  def initialize
    @order = 0
    @matrix = []
  end

  def add_vertex
    @order += 1
    @matrix.each do |vert|
      vert << 0
    end
    @matrix << [0]*@order
  end

  def add_edge(from, to)
    @matrix[from][to] = 1
    @matrix[to][from] = 1
  end

  def print_graph
    @matrix.length.times do |i|
      vert = @matrix[i]
      vert.length.times do |j|
        if (@matrix[i][j] == 1)
          puts "(" + i.to_s + "," + j.to_s + ")"
        end
      end
    end
  end

end

def bfs(graph, start_key)
  start = graph.get_vertex(start_key)
  visited = Hash[graph.vertices.values.collect {|v| [v,false].flatten}]
  q = Queue.new

  q.enqueue(start)
  while (q.size > 0)
    v = q.dequeue
    if (!visited[v])
      visited[v] = true
      puts v.key
      v.neighbours.each do |nbr,_|
        q.enqueue(nbr)
      end
    end
  end
end


def dfs(graph, start_key)
  start_vertex = graph.get_vertex(start_key)
  visited = Hash[graph.vertices.values.collect {|v| [v,false].flatten}]
  _dfs(start_vertex, visited)
end

def _dfs(start_vertex, visited)
  visited[start_vertex] = true
  start_vertex.neighbours.each do |vert,_|
    if (!visited[vert])
      puts start_vertex.key.to_s + "->" + vert.key.to_s
      _dfs(vert, visited)
    end
  end
end


def dfs_non_recursive(graph, start_key)
  start_vertex = graph.get_vertex(start_key)
  visited = Hash[graph.vertices.values.collect {|v| [v,false].flatten}]  
  s = Stack.new

  s.push(start_vertex)
  while (!s.is_empty?)
    v = s.pop
    if (!visited[v])
      puts v.key.to_s
      visited[v] = true
      v.neighbours.each do |vert,_|
        s.push(vert)
      end
    end
  end
    
end

def has_cycle_directed?(graph)
  graph.vertices.each do |_, vert|
    visited = Hash[graph.vertices.values.collect {|v| [v,false].flatten}]
    return true if _cycle_detect(vert, visited)
  end
  return false
end

def _cycle_detect_directed(start_vertex, visited)
  if (visited[start_vertex])
    return true
  else
    visited[start_vertex] = true
    start_vertex.neighbours.each do |vert,_|
      if (_cycle_detect(vert, visited))
        return true
      end
    end
    return false
  end
end


def has_cycle_undirected?(graph)
  graph.vertices.each do |_, vert|
    visited = Hash[graph.vertices.values.collect {|v| [v,false].flatten}]
    return true if _cycle_detect_undirected(vert, visited, nil)
  end
  return false  
end


def _cycle_detect_undirected(start_vertex, visited, parent)
  visited[start_vertex] = true
  start_vertex.neighbours.each do |vert,_|
    if (!visited[vert])
      if (_cycle_detect_undirected(vert, visited, start_vertex))
        return true
      end
    elsif (vert != parent)
      return true
    end
  end
  return false
end

# prim's alg to find MST
# 0 -> unseen
# 1 -> fringe
# 2 -> intree
def prims(graph)
  start = graph.getVertex # assume returns arbitrary vertex in graph
  pq = PriorityQueue.new
  pq.enqueue(0, start)
  start.set_status(2)
  start.set_parent(nil)
  mst = Graph.new
  
  while (!pq.empty?)
    current = pq.dequeue
    current.set_status(2)
    mst.add_vertex(current)
    mst.add_edge(current, current.parent) if !current.parent.nil?
    current.getNeighbours.each do |neighbour|
      if (neighbour.get_status == 0)
        # found new unseen vertex
        neighbour.set_status(1)
        neighbour.set_parent(current)
        pq.enqueue(current.neighbours[neighbour], neighbour)
      elsif (neighbour.get_status == 1)
        # encountered previously seen fringe vertex
        current_edge_weight = pg.get_priority(neighbour)
        new_edge_weight = current.neighbours[neighbour]
        if (new_edge_weight < current_edge_weight)
          # found smaller weight edge, so update
          neighbour.set_parent(current)
          pq.update_priority(new_edge_weight, current)
        end
#        current_weight = neighbour.get_pqweight
#        if (current.neighbours[neighbour] < current_weight)
          # found smaller weight edge, so update
#        end
      end
    end
  end
  return mst
end


def dijkstras(graph, s)
  pq = PriorityQueue.new
  graph.get_vertices.each do |vertex|
    vertex.set_distance(1.0/0.0)
    vertex.set_parent(nil)
    pq.enqueue(vertex, vertex.get_distance)
  end
  path_tree = Graph.new

  start.set_distance(0)
  pq.update_priority(start, start.get_distance)
  
  for i in (0..graph.order()) do
    current_vert = pq.enqueue
    path_tree.add_vertex(current_vert)
    path_tree.add_edge(current_vert, current_vert.parent) if !current_vert.parent.nil?
    # add current_vert to path tree
    current_vert.get_neighbours.each do |neighbour|
      if (neighbour not in path_tree)
        neighbour_distance = neighbour.get_distance
        if (current_vert.get_distance + current_vert.neighbours[neighbour] < neighbour_distance)
          # update accordingly
          neighbour.set_distance(current_vert.get_distance + current_vert.neighbours[neighbour])
          neighbour.set_parent(current_vert)
          pq.update_priority(neighbour, neighbour.get_distance)
        end
      end
    end
  end
  return path_tree
    
end



#begin
#  g = Graph.new
#  g.add_vertex("a")
#  g.add_vertex("b")
#  g.add_vertex("c")
#  g.add_edge("a", "b")
#  g.add_edge("a", "c")
#  g.add_edge("c", "b")
#  g.print_graph
  #bfs(g, "a")
#  puts has_cycle_undirected?(g)

#  puts ""
#end
"""
  d = DiGraph.new
  d.add_vertex(0)
  d.add_vertex(1)
  d.add_vertex(2)
  d.add_vertex(3)

  d.add_edge(2,0)
 # d.add_edge(0,2)
  d.add_edge(0,1)
#  d.add_edge(1,2)
  d.add_edge(2,3)
  #d.add_edge(3,3)
  bfs(d,2)
 # puts ""
  dfs(d,1)
  puts ""
  #puts has_cycle?(d)
#  dfs_non_recursive(d,1)
end


  #g = AdjMatrixGraph.new
  #g.add_vertex
  #g.add_vertex
  #g.add_vertex
  #g.add_edge(0,1)
  #g.add_edge(0,2)
  #g.add_edge(1,2)
  #g.print_graph
#end
"""
