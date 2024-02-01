from django.shortcuts import render, redirect
from django.contrib import messages
from mysite.mysite.forms import DateForm
from mysite.mysite.utils import search_in_google_sheets

def detect_anomalies(request):
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            selected_date = form.cleaned_data['date']

            try:
                detected_value = search_in_google_sheets(selected_date)
                print(f"Detected value for {selected_date}: {detected_value}")
            except Exception as e:
                # Handle the exception, you might want to log the error
                detected_value = None
                error_message = f"An error occurred: {str(e)}"
                messages.error(request, error_message)
                print(f"Error in view: {error_message}")
                return redirect('detect_anomalies')

            if detected_value is not None:
                print(f"Detected values for {selected_date}: {detected_value}")
                # Render the anomalies result template with form and detected value
                messages.success(request, f"Anomalies detected for {selected_date}")
                print(f"Rendering anomalies_result.html for {selected_date}")
                return render(request, 'anomalies_result.html', {'form': form, 'detected_value': detected_value})
            else:
                no_result_message = f"No result found for {selected_date}."
                messages.info(request, no_result_message)
                print(f"No result found for {selected_date}")
                return redirect('detect_anomalies')
    else:
        form = DateForm()

    return render(request, 'detect_anomalies.html', {'form': form})








