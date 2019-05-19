using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BoxyMovement : MonoBehaviour
{
    // That's a up lmao, get it?
    // Float... up?
    public float up;
    private Rigidbody2D rb2D;
    private IEnumerator rotateLeftCoroutine;
    private IEnumerator rotateRightCoroutine;
    private bool rotateLeft;
    private bool rotateRight;
    // Keeps track of the angle at which we need to switch rotation
    private float currentAngle;

    void Start()
    {
        rb2D = GetComponent<Rigidbody2D>();
        rotateLeftCoroutine = rotateLeftSubroutine();
        rotateRightCoroutine = rotateRightSubroutine();
        rotateLeft = true;
        rotateRight = false;
        currentAngle = 0f;
    }

    // Because it is the right thing to do :P
    void FixedUpdate()
    {
        // If we press `spacebar`, we expect the box to float up!
        // Let's test it out!
        // USE GetKeyDown instead!
        // GetKey checks if spacebar is pressed down
        // GetKeyDown checks if space has been clicked!!
        if (Input.GetKeyDown("space"))
        {
            // Vector3 is (x, y, z)
            // Don't worry about 'z' in 2d, it does nothing
            rb2D.velocity = new Vector3(0.0f, up, 0.0f);
            rotateLeft = !rotateLeft;
            rotateRight = !rotateRight;
            if (rotateLeft)
            {
                // Starts left rotation and does not stop unless
                // the function ends or stop coroutine is called.
                // In our case, will not end because our functions
                // have infinite while loops and never return
                // For this reason, we need to stop the routines ourselves
                StartCoroutine(rotateLeftCoroutine);
                StopCoroutine(rotateRightCoroutine);
            }
            else
            {
                StartCoroutine(rotateRightCoroutine);
                StopCoroutine(rotateLeftCoroutine);
            }
        }
    }

    IEnumerator rotateLeftSubroutine()
    {
        while (rotateLeft)
        {
            currentAngle += 3.6f;
            rb2D.MoveRotation(currentAngle);
            // otherwise runs too fast!
            yield return new WaitForSeconds(0.0001f);
        }
    }

    IEnumerator rotateRightSubroutine()
    {
        while (rotateRight)
        {
            currentAngle -= 3.6f;
            rb2D.MoveRotation(currentAngle);
            // otherwise runs too fast!
            yield return new WaitForSeconds(0.0001f);
        }
    }
}
