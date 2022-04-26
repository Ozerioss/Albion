function sellItems()
  -- For debugging purposes
  --x, y = GetMousePosition();
  --OutputLogMessage("Mouse is at %d, %d\n", x, y);
  sell()
  undercut()
  create_sell_order()
end

function initSell()
  sell()
  moveNclick(19124, 31401) -- sell order only once per loop of full inventory
  undercut()
  create_sell_order()
end

function sell()
  moveNclick(43713, 26117)
end

function undercut()
  moveNclick(19261, 38750)
end

function create_sell_order()
  moveNclick(30394, 44034)
end


function moveNclick(x, y)
  MoveMouseTo(x, y)
  Sleep(500)
  PressMouseButton(1)
  Sleep(50)
  ReleaseMouseButton(1)
  Sleep(500)
end

function OnEvent(event, arg)
    OutputLogMessage("Event: "..event.." Arg: "..arg.."\n")
    if event == "MOUSE_BUTTON_PRESSED" and arg == 3
    then
      for item_index = 1, 48, 1
      do
        if item_index == 1
        then
          initSell()
        end
        OutputLogMessage("Selling item %d of 48\n", item_index)
        sellItems()
      end
    end
end