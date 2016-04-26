class Node

  def initialize(data)
    @data = data
    @next_node = nil
  end

  def get_data
    return @data
  end

  def get_next
    return @next_node
  end

  def set_data(data)
    @data = data
  end

  def set_next(node)
    @next_node = node
  end

end


class CircularLinkedList

  def initialize
    @head = nil
  end

  def add(item)
    if (@head.nil?)
      temp = Node.new(item)
      temp.set_next(temp)
      @head = temp
      return
    end

    start = @head
    current = @head.get_next
    previous = start

    while (current != start)
      previous = current
      current = current.get_next
    end

    temp = Node.new(item)
    temp.set_next(@head)
    @head = temp
    previous.set_next(temp)
  end

  def length
    if (is_empty?)
      return 0
    end

    count = 1 # at least one item
    start = @head
    current = @head.get_next

    while (current != start)
      count += 1
      current = current.get_next
    end

    return count
  end

  def is_empty?
    return @head.nil?
  end

  def remove(item)
    start = @head
    previous = start
    current = start.get_next
    found = false

    loop do
    #while (current != start and not found)
      if (current.get_data == item)
        found = true
      else
        previous = current
        current = current.get_next
      end
      break if (found or current == start)
    end

    if (not found)
      return false
    end


    if (current == start)
      # deleting first item
      if (previous == start)
        # deleting first item from length 1 list
        @head = nil
      else
        # deleting first item from length > 1 list
        @head = current.get_next
        previous.set_next(current.get_next)
      end
    else
      # remove like in singly linked list
      previous.set_next(current.get_next)
    end
  end

  def search(item)
    if (is_empty?)
      return false
    end

    start = @head
    current = start
    found = false
    
    loop do
      if (current.get_data == item)
        found = true
      else
        current = current.get_next
      end
      break if (found or current == start)
    end

    return found
  end

  def append(item)
    if (is_empty?)
      add(item)
      return
    end

    start = @head
    current = start
    previous = start
    
    loop do
      previous = current
      current = current.get_next
      break if (current == start)
    end

    temp = Node.new(item)
    temp.set_next(start)
    previous.set_next(temp)
  end

  def index(item)
    start = @head
    current = start
    pos = 0
    found = false

    loop do
      if (current.get_data == item)
        found = true
      else
        pos += 1
        current = current.get_next
      end
      break if (found or current == start)
    end
    
    if (found)
      return pos
    else
      return false
    end
  end

  def insert(pos, item)
    if (pos == 0)
      add(item)
      return
    end
    
    start = @head
    current = start
    previous = start
    current_pos = 0
    
    while (current_pos != pos)
      previous = current
      current = current.get_next
      current_pos += 1
    end

    temp = Node.new(item)
    temp.set_next(current)
    previous.set_next(temp)
  end

  def pop(pos=(length-1))
    start = @head
    current = start
    previous = start
    current_pos = 0

    while (current_pos != pos)
      previous = current
      current = current.get_next
      current_pos += 1
    end

    if (current == start)
      # popping first item
      if (@head.get_next == start)
        # popping first item from length 1 list
        @head = nil
        return start.get_data
      else
        # need to traverse to end to update end pointer
        current = start.get_next
        while (current != start)
          previous = current
          current = current.get_next
        end
        previous.set_next(start.get_next)
        @head = start.get_next
        return start.get_data
      end
    else
      previous.set_next(current.get_next)
      return current.get_data
    end
  end

end


begin
  l = CircularLinkedList.new
  l.add(12)
  l.add(13)
  l.add(15)
  puts l.inspect
  puts l.length
  puts l.pop(1)
  puts l.inspect
end
