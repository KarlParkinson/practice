require_relative 'heap.rb'

class PriorityQueue

  def initialize
    @items = MaxHeap.new
  end

  def enqueue(k)
    @items.insert(k)
  end

  def dequeue
    val = @items.find_max
    @items.del_max
    return val
  end

  def is_empty?
    @items.is_empty
  end

  def size
    @items.size
  end

end
