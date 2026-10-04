<!---
If you're new to markdown, check out this reference: https://www.markdownguide.org/basic-syntax/
-->

# Writeup

## Q0. Investigating Transforms in Foxglove (10 pts)

**Q0.1:**

## Q1. Identifying a Kinematic Model (20 pts)

**Q1.1:** 

<!---
You can use LaTeX syntax like so: $a_{example} = b_{example} + c_{example}$.
You can use $\upsilon$ for linear velocity and $\omega$ for angular velocity.

If you prefer to write out your work, you can include it in an image as follows:
![image description](./image_path.png)
-->
Given target linear velocity $\upsilon$ (m/s), angular velocity $\omega$ (rad/s), and wheel separation $b$ (m).

From lecture, we have

$$
\upsilon = \frac{\upsilon_r + \upsilon_l}{2}.
$$

Suppose the robot is turning with $r$ being the distance from the body frame to the instantaneous center of robot rotation. For a counterclockwise turn, the left wheel follows a radius of curvature of $r - \frac{b}{2}$ and the right wheel follows a radius of curvature of $r + \frac{b}{2}$.

Then,

$$
\upsilon_l = \omega\left(r - \frac{b}{2}\right)
\qquad
\upsilon_r = \omega\left(r + \frac{b}{2}\right).
$$

Then,

$$
\frac{\upsilon_l}{\omega} + \frac{b}{2}
=
\frac{\upsilon_r}{\omega} - \frac{b}{2}
\qquad \Rightarrow \qquad
\omega = \frac{\upsilon_r - \upsilon_l}{b}.
$$

Then,

$$
\frac{\omega}{\upsilon}
=
\frac{2(\upsilon_r - \upsilon_l)}
{(\upsilon_r + \upsilon_l)b}.
$$

So,

$$
\upsilon_l = \upsilon - \frac{b\omega}{2}
\qquad
\upsilon_r = \upsilon + \frac{b\omega}{2}.
$$


**Q1.2:**

We know that $\upsilon = r\dot{\phi}$ and $r = \frac{d}{2}$.

Given $\upsilon_l$ and $\upsilon_r$,

$$
\upsilon_l = r\dot{\phi}_l
\qquad
\upsilon_r = r\dot{\phi}_r.
$$

Solving for $\dot{\phi}_l$ and $\dot{\phi}_r$, we get

$$
\dot{\phi}_l = \frac{\upsilon_l}{r}
\qquad
\dot{\phi}_r = \frac{\upsilon_r}{r}.
$$

Since $r = \frac{d}{2}$,

$$
\dot{\phi}_l = \frac{2\upsilon_l}{d}
\qquad
\dot{\phi}_r = \frac{2\upsilon_r}{d}.
$$


**Q1.3:**

From Q1.1, we have

$$
\upsilon_l = \upsilon - \frac{b\omega}{2}
\qquad
\upsilon_r = \upsilon + \frac{b\omega}{2}.
$$

Adding the two equations,

$$
\upsilon_l + \upsilon_r = 2\upsilon
$$

so

$$
\upsilon = \frac{\upsilon_r + \upsilon_l}{2}.
$$

Subtracting the left wheel velocity from the right wheel velocity,

$$
\upsilon_r - \upsilon_l = b\omega
$$

so

$$
\omega = \frac{\upsilon_r - \upsilon_l}{b}.
$$

Here, $b$ is the wheel separation. This follows the sign convention that a left turn has $\upsilon_r > \upsilon_l$, giving $\omega > 0$, while a right turn has $\upsilon_r < \upsilon_l$, giving $\omega < 0$.

## Q2. Inverse Kinematics (20 pts)

**Q2.2:** 

**Q2.3:** 

## Q3. Forward Kinematics (20 pts)

**Q3.2:** 

## Q4. Calculating an Odometry Solution (30 pts)

**Q4.3:** 


## Feedback

**How much time did you spend on this assignment?** 

**Do you have any feedback for this assignment?**
