class MaxHeap

  def initialize
    @keys = []
  end

  def insert(i)
    @keys << i
    perc_up(@keys.length-1)
  end

  def find_max
    return @keys[0]
  end

  def del_max
    @keys[0] = @keys[@keys.length - 1]
    @keys.pop
    perc_down(0)
  end

  def is_empty
    return @keys.empty?
  end

  def size
    return @keys.length
  end

  def build_heap(arr)
    @keys = arr
    ind = arr.length / 2
    while (ind >= 0)
      perc_down(ind)
      ind -= 1
    end
  end

  private

  def perc_up(ind)
    while ((ind-1)/2 >= 0)
      if (@keys[ind] > @keys[(ind-1)/2])
        tmp = @keys[(ind-1)/2]
        @keys[(ind-1)/2] = @keys[ind]
        @keys[ind] = tmp
      end
      ind = (ind-1)/2
    end
  end

  def perc_down(ind)
    while ((ind * 2) + 1 < @keys.length)
      mc = get_max_child(ind)
      if (@keys[ind] < @keys[mc])
        tmp = @keys[ind]
        @keys[ind] = @keys[mc]
        @keys[mc] = tmp
      end
      ind = mc
    end
  end

  def get_max_child(ind)
    if ((ind*2) + 2 > @keys.length-1)
      return ind*2 + 1
    else
      if (@keys[ind*2 + 1] > @keys[ind*2 + 2])
        return ind*2 + 1
      else
        return ind*2 + 2
      end
    end
  end

end
