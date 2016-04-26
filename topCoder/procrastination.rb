def findFinalAssignee(n)
  emp = n # initially assigned to employee n
  hour = 2
  while ((hour**2) <= emp+1)
    if (emp % hour == 0)
      emp += 1
    elsif ((emp-1) % hour == 0)
      emp -= 1
    end
    hour += 1
  end

  hour -= 1
  last_hour = hour
 # puts emp
  while (hour > 1)
    hh = emp/hour
#    puts hh
    if (hh <= last_hour)
      hour -= 1
      next
    end
    if (hh < emp and emp%hh == 0)
      emp += 1
    elsif (emp%hh == 1 and n/hh > 1)
      emp -= 1
    end
    hour -= 1
  end
  return emp
end

begin
  #puts findFinalAssignee(8)
  puts findFinalAssignee(5587021440)
end
