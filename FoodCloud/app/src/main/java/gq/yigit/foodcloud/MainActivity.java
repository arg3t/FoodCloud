/*
PAUSE FOR PRAYER

Dear God,
Please help me find any malicious bugs that I've created
and ,yet, I can't spot.
Make my code free of errors.


END PRAYER
*/

package gq.yigit.foodcloud;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import com.google.zxing.integration.android.IntentIntegrator;
import com.google.zxing.integration.android.IntentResult;
import android.content.Intent;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import java.util.HashMap;


public class MainActivity extends AppCompatActivity implements OnClickListener{
    private static final String TAG = "MainActivity";
    int cnt = 0;
    private Button scanBtn;
    private Button infoBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        System.gc();
        scanBtn = (Button)findViewById(R.id.scan_button);

        scanBtn.setOnClickListener(this);
        infoBtn = (Button)findViewById(R.id.info_button);

        infoBtn.setOnClickListener(this);

    }

    public void onClick(View v){
            if (v.getId() == R.id.scan_button) {
                IntentIntegrator scanIntegrator = new IntentIntegrator(this);
                scanIntegrator.initiateScan();

            }
        if (v.getId() == R.id.info_button) {
            startActivity(new Intent(MainActivity.this, GetInfo.class));

        }


    }

    public void onActivityResult(int requestCode, int resultCode, Intent intent) {
        IntentResult scanningResult = IntentIntegrator.parseActivityResult(requestCode, resultCode, intent);
        String scanContent = scanningResult.getContents();
        try{
            scanContent.toString();
            Intent i = new Intent(MainActivity.this, ProductInfo.class);
            i.putExtra("key",scanContent);
            startActivity(i);
        }
        catch(NullPointerException e) {
            Toast toast = Toast.makeText(getApplicationContext(),
                    "No scan data received!", Toast.LENGTH_SHORT);
            toast.show();
        }catch(RuntimeException e){
            Toast toast = Toast.makeText(getApplicationContext(),
                    "No scan data received!", Toast.LENGTH_SHORT);
            toast.show();
        }

    }
}
