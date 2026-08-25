from client import RealtimeCanvasBrushLatentImageEnhancerClient

def main():
    client = RealtimeCanvasBrushLatentImageEnhancerClient()
    res = client.enhance_canvas_sketch_stream(32, 80.0, '8X_NEURAL_UPSCALE')
    print('Canvas Session: ' + res['canvas_session_id'] + ' (Latency: ' + str(res['canvas_render_latency_ms']) + 'ms)')
    print('Detail Score: ' + str(res['high_frequency_texture_detail_score']) + '/100 | Mode: ' + res['upscale_multiplier'])
    print('Canvas URL: ' + res['enhanced_tensor_canvas_url'])

if __name__ == '__main__':
    main()
