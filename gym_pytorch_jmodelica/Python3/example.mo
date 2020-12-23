model example

   parameter Real a_ove=10;
   parameter Boolean a_ove_activate=true;
   parameter Real a = if a_ove_activate then a_ove else 5;

   ode eqn(a=a);

  model ode
    parameter Real  a;

    Real x(start=0);

  equation
    der(x) = a;

  end ode;

end example;
