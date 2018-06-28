package gq.yigit.foodcloud;

import android.content.DialogInterface;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebView;
import android.widget.Button;

public class GetInfo extends AppCompatActivity implements View.OnClickListener {
    public  Button back_to_main;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_get_info);
        WebView myWebView = (WebView) findViewById(R.id.info);
        myWebView.loadUrl("https://www.welthungerhilfe.org/our-work/approaches/food-security-standard/");
        back_to_main = (Button) findViewById(R.id.back_to_main);
        back_to_main.setOnClickListener(this);
    }
    public void onClick(View v){

            onBackPressed();
            Intent i = new Intent(GetInfo.this, MainActivity.class);
            startActivity(i);
    }
}
